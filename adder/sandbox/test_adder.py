import random
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_basic_adder(dut):
    """Test our adder against Python addition."""
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