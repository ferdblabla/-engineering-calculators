def voltage_drop_dc(current_a, length_m, resistance_ohm_per_m):
    """Calculate round-trip DC cable voltage drop in volts."""
    return current_a * (2 * length_m * resistance_ohm_per_m)


def drop_percent(source_voltage, drop_voltage):
    if source_voltage == 0:
        raise ValueError("Source voltage cannot be zero.")
    return (drop_voltage / source_voltage) * 100


if __name__ == "__main__":
    source_v = 24.0
    current = 2.0
    cable_length = 15.0
    resistance_per_m = 0.008

    drop = voltage_drop_dc(current, cable_length, resistance_per_m)
    print(f"Voltage drop: {drop:.2f} V")
    print(f"Drop percentage: {drop_percent(source_v, drop):.2f}%")
