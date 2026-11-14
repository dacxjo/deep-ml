def calculate_parameters(layers: list[dict]) -> int:
    """
    Calculate the total number of trainable parameters in a neural network.

    Args:
        layers: List of dictionaries, each describing a layer.

    Returns:
        Total number of trainable parameters (int).
    """
    # Your code here
    total = 0
    for item in layers:
        if item['type'] == "dense":
            total += item['input_size'] * item['output_size']
            if 'bias' not in item or item["bias"] == True:
                total += item['output_size']
        elif item["type"] == "conv2d":
            temp = item['in_channels']*item['out_channels']*item['kernel_size']*item['kernel_size']
            if item["bias"] == True:
                total += temp + item['out_channels']


    return total