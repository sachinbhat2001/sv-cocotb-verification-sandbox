import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ReadOnly, RisingEdge, Timer


@cocotb.test()
async def test_counter(dut):
    """Verify synchronous reset, up-counting, and 4-bit rollover (15 -> 0)."""
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # 1. Assert reset across a rising clock edge
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.q.value) == 0, f"Expected 0 after reset, got {int(dut.q.value)}"

    # 2. Release reset after stepping out of ReadOnly
    await Timer(1, unit="ns")
    dut.rst.value = 0

    # 3. Run 20 clock cycles so we see 1..15 and wrap-around back to 0..3
    expected = 0
    for cycle in range(20):
        await RisingEdge(dut.clk)
        await ReadOnly()
        expected = (expected + 1) % 16
        actual = int(dut.q.value)
        dut._log.info(f"Cycle {cycle}: q={actual} (expected {expected})")
        assert actual == expected, f"Mismatch at cycle {cycle}: got {actual}, expected {expected}"
        await Timer(1, unit="ns")
