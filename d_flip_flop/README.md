# RTL Verification: 1-Bit D Flip-Flop (`dff.v`)

An incremental sequential RTL design and verification exercise using **Verilog**, **Verilator** (C++ simulation compilation), **cocotb** (Python testbenches), and **GTKWave** (waveform analysis), automated via a `Makefile`.

## Methodology

* **Verilator:** Compiles Verilog RTL into a C++ simulation model (`sim_build/Vtop`) linked with `cocotb`'s VPI interface.
* **cocotb:** Drives synchronous reset and randomized data stimulus across clock edges using `Clock`, `RisingEdge`, `ReadOnly`, and `Timer` triggers.
* **GTKWave:** Inspects recorded clock-edge transitions (`dump.vcd`) to verify synchronous reset priority and edge-triggered state updates.

## RTL Design (`sandbox/dff.v`)

* **Inputs:** `clk` (1-bit positive-edge clock), `rst` (1-bit active-high synchronous reset), and `d` (1-bit data input)
* **Output:** `q` (1-bit registered state output)
* **Behavior:** Positive-edge-triggered sequential logic (`always @(posedge clk)`) using non-blocking assignments (`<=`) to clear `q` when `rst` is high and capture `d` otherwise


```verilog
module dff (
    input  wire clk,
    input  wire rst,
    input  wire d,
    output reg  q
);
    always @(posedge clk) begin
        if (rst) begin
            q <= 1'b0;
        end else begin
            q <= d;
        end
    end
endmodule
