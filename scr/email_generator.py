import logging
from dotenv import load_dotenv

from openai import OpenAI
from .utils import get_config_params


logger = logging.getLogger(__name__)
load_dotenv()  # load env variables from .env
# Log in to Hugginb face using your token.

config = get_config_params()  # Load config
client = OpenAI()


class EmailGenerator:

    def __init__(
            self,
            email_template: str,
            personalization_map: dict
    ):
        # init the api key in OPEN AI
        # This will "log you in" Open AI
        self.email_template = email_template
        self.personalization_map = personalization_map
        self._model_params = self._load_model_params

    @property
    def _load_model_params(self):
        return config["model_params"]

    def generate_email(
        self
    ):

        prompt = (
            "You are working in the marketing department of a Spanish inen speciality store."
            "You are tasked with writing emails for the top clients, following these instructions: "
            f"Generate a variation of this email replacing [NAME] with {self.personalization_map['name']}"
            f" and [LOC] with {self.personalization_map['province']}."
            f" make it {self.personalization_map.get('style', 'formal')}"
            " the brand name is Top Linen"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
            ],
            **config['model_params']

        )
        return response.choices[0].message.content
