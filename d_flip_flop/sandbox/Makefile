SIM ?= verilator
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/dff.v
TOPLEVEL = dff
COCOTB_TEST_MODULES = test_dff
EXTRA_ARGS += --trace

include $(shell cocotb-config --makefiles)/Makefile.sim