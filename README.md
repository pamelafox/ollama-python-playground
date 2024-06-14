# Ollama Python Playground

This project is designed to be opened in GitHub Codespaces as an easy way for anyone to try out SLMs (small language models) entirely in the browser.

1. Open the Codespace in the browser using the `Code` button at the top of the repository.
2. Once the Codespace is loaded, it should have [ollama]() pre-installed as well as the [OpenAI Python SDK]().
3. Ask Ollama to run the SLM of your choice. For example, to run phi3:

    ```shell
    ollama run phi3:mini
    ```

    That will take a few minutes to download the model into the Codespace.
4. Once you see "success" in the output, you can send a message to that model from the prompt.

    ```shell
    >>> Write a haiku about hungry hippos
    ```

5. After several seconds, you should see a response stream in from the model.
6. To learn about different techniques used with language models, open the Python notebook `ollama.ipynb` and run each cell . If you used a model other than 'phi3:mini', change the `MODEL_NAME` in the first cell.
7. To have a conversation with a model from Python, open the Python file `chat.py` and run it. You can change the `MODEL_NAME` at the top of the file as needed, and you can also modify the system message or add few-shot examples if desired.


