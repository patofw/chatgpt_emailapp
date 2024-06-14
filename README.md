# Personalized Email Generator App

## Powered with OPEN AI & CHATGPT!

This is a simple yet powerful personalised email generator app, powered by OpenAI's ChatGPT. 

## 1. Installation. 
- Create a Python virtual environment (recommended). 
- Clone this repo
   `git clone https://github.com/patofw/chatgpt_emailapp.git`
- Add your OpenAI api key to your .env:
  Follow the template in `.env_example` but do it in your local `.env` file. 
  
  For questions in how to create and locate your OpenAI api key follow this [link](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key). 
- install the `build` package:  ```pip install --upgrade build```
- install the `setuptools` package: ```pip install --upgrade setuptools```

- Build the Python module:
  
  `python -m build`
  
  and then
  
  `pip install -e .` 

# 2. Context of this repo. 

This is a simple tutorial in how to leverage the use of LLMs in business applications. For this toy example, we want to have ChatGPT create personalised emails for a list of clients, based on an original email template. 

For this example, I have set up a fake Linen clothes shop in Spain that is aiming to promote their new collection to a selected group of clients. 

The app will create a unique personalised email for each client based on some attributes given by the user.

# 3. Working example. 

To make it work, simply follow these steps: 
  1. Under the `input` folder, fill out the sample customer list. 
  2. On the same folder, add the `email template`. 
  3. Head to the `config.yaml` file and set up the correct paths and parameters.
  4. Once everything is set, simply run ```streamlit run emailapp.py```
  5. Follow the simple Streamlit's App instructions and generate the personalised emails. The ouputs will be saved on the given path set up in the `config.yaml` 
  6. If you want to add more personalization details simply crete new columns in the input dataset and make sure you add this in the template, following this example: 

Say you want to add the `profession` of the client. You would need to create the `profession` column in the dataset and similarly add "[PROFESSION]" to the template. Finally, modify the prompt in `scr/email_generator.py`. 

```python
prompt = (

            f"Generate a variation of this email replacing [NAME] with {self.personalization_map['name']}"
            f" and [LOC] with {self.personalization_map['province']}."
            f" and [PROFESSION] with {self.personalization_map['profession']"
            f" make it {self.personalization_map.get('style', 'formal')}"
            " the brand name is Top Linen"
        )
```

# Next Steps. 

The Streamlit app is extremly basic and only meant to show the functionality of the `email_generator.py` engine. You could imagine building a much more complex app to fit your business neeeds. 

