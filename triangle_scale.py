def scaled_height(original_base, original_height, new_base):
    """Return the height of a similar triangle after scaling its base."""
    if original_base == 0:
        raise ValueError("Original base cannot be zero.")
    scale_factor = new_base / original_base
    return original_height * scale_factor


if __name__ == "__main__":
    base = 12.5
    height = 3.05
    new_base = 6.0
    result = scaled_height(base, height, new_base)
    print(f"Scaled height: {result:.3f}")
