import yaml
import pandas as pd


def get_config_params():
    """Opens a yaml config file and loads it.

    Returns:
        Config dictioary
    """
    with open("./config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


def load_inputs(config) -> (str, pd.DataFrame):
    """Loads the inputs necessary for the emailapp.

    Args:
        config (_type_): configuration YML file loaded.

    Returns:
        email template string and customer dataframe
        _type_: Tuple[str, pd.DataFrame]
    """
    with open(config["template_email_path"], "r") as f:
        email_template = f.read()
    customer_df = pd.read_csv(
        config['input_csv']
    )
    return email_template, customer_df
