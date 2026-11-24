# RTL Verification: 8-Bit Combinational Adder (`adder.sv`)

An incremental RTL design and verification exercise using **SystemVerilog**, **Verilator** (C++ simulation compilation), **cocotb** (Python testbenches), and **GTKWave** (waveform analysis), automated via a `Makefile`[cite: 1, 2, 3, 5].

## Methodology

* **Verilator:** Compiles SystemVerilog RTL into a C++ simulation model (`sim_build/Vtop`) linked with `cocotb`'s VPI interface[cite: 1, 5].
* **cocotb:** Drives randomized test vectors and checks assertions in Python across `await` simulation boundaries (`Timer`)[cite: 1, 5].
* **GTKWave:** Inspects recorded signal transitions (`dump.vcd`) with decimal/unsigned formatting[cite: 1, 3, 5].

## RTL Design (`sandbox/adder.sv`)

* **Inputs:** `a [7:0]` and `b [7:0]` (8-bit unsigned operands)[cite: 1, 5]
* **Output:** `sum [8:0]` (9-bit unsigned sum, supporting values up to `510` without 8-bit wraparound)[cite: 1, 5]
* **Behavior:** Pure combinational continuous assignment (`assign sum = a + b;`) with no clock or flip-flops[cite: 1, 5]

```systemverilog
module adder (
    input  logic [7:0] a,
    input  logic [7:0] b,
    output logic [8:0] sum
);
    assign sum = a + b;
endmodule
```

## Project Structure

```text
.
├── .gitignore
├── README.md
├── docs/
│   └── waveform.png
└── sandbox/
    ├── adder.sv
    ├── test_adder.py
    └── Makefile
```

## Testbench (`sandbox/test_adder.py`)

```python
import random
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_basic_adder(dut):
    """Verify 8-bit unsigned adder outputs against a Python reference model."""
    for i in range(10):
        val_a = random.randint(0, 255)
        val_b = random.randint(0, 255)

        dut.a.value = val_a
        dut.b.value = val_b

        await Timer(10, unit="ns")

        hw_sum = int(dut.sum.value)
        expected = val_a + val_b
        dut._log.info(f"Test {i}: {val_a} + {val_b} = {hw_sum} (expected {expected})")
        assert hw_sum == expected, f"Mismatch! Got {hw_sum}, expected {expected}"
```

## Running & Inspecting Waveforms

```bash
cd sandbox
source ../.venv/bin/activate
make
```

To open the generated VCD file in GTKWave:

```bash
gtkwave dump.vcd &
```

Select `adder` in the SST panel, append `a[7:0]`, `b[7:0]`, and `sum[8:0]`, zoom to fit, and set the signal radix to **Unsigned** or **Decimal**[cite: 5].

![GTKWave 8-bit Adder Waveform](adder/docs/adder_waveform.png)

## Next Milestone

Transition from combinational logic to sequential design by implementing a **4-bit synchronous counter (`counter.sv`)** in `sandbox/` to practice `clk`, `rst`, `always_ff`, non-blocking assignments (`<=`), and `RisingEdge(dut.clk)`.
