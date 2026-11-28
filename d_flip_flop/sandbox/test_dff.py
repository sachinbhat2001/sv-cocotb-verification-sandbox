import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ReadOnly, RisingEdge, Timer


@cocotb.test()
async def test_dff(dut):
    """Verify synchronous reset and rising-edge sampling on a 1-bit D flip-flop."""
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Assert synchronous reset across a clock edge
    dut.d.value = 0
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    #await RisingEdge(dut.clk)
    assert int(dut.q.value) == 0, f"Expected q=0 during reset, got {int(dut.q.value)}"

    # Release reset and check sampled values on each rising clock edge
    await Timer(1, unit="ns")
    dut.rst.value = 0
    for cycle in range(10):
        val_d = random.randint(0, 1)
        dut.d.value = val_d
        await RisingEdge(dut.clk)
        await ReadOnly()
        actual_q = int(dut.q.value)
        dut._log.info(f"Cycle {cycle}: d={val_d} -> q={actual_q}")
        assert actual_q == val_d, f"Mismatch at cycle {cycle}: got q={actual_q}, expected {val_d}"
        await Timer(1, unit="ns")
