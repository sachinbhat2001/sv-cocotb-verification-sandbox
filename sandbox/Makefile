SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/adder.sv
TOPLEVEL = adder
COCOTB_TEST_MODULES = test_adder

EXTRA_ARGS += --trace

include $(shell cocotb-config --makefiles)/Makefile.sim