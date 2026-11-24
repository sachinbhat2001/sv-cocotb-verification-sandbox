# 8-Bit Combinational Adder (`adder.sv`)

A minimal RTL verification exercise implementing an 8-bit unsigned combinational adder in SystemVerilog, compiled to C++ via **Verilator**, driven and checked in Python with **cocotb**, and inspected visually in **GTKWave**.

## Architecture & RTL Design
- **Inputs:** `a [7:0]` and `b [7:0]` (8-bit unsigned operands)
- **Output:** `sum [8:0]` (9-bit unsigned sum, supporting values up to `511` without 8-bit wraparound)
- **Behavior:** Pure combinational continuous assignment (`assign sum = a + b;`) with no clock or flip-flops

## Project Structure
- `sandbox/adder.sv` — SystemVerilog RTL module
- `sandbox/test_adder.py` — `cocotb` verification testbench
- `sandbox/Makefile` — Verilator + `cocotb` build and simulation rules

## Running the Simulation
```bash
cd sandbox
source ../.venv/bin/activate
