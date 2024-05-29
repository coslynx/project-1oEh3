```python
# customizable_responses.py

class CustomizableResponses:
    def __init__(self):
        self.custom_responses = {}

    def add_custom_response(self, trigger, response):
        self.custom_responses[trigger] = response

    def remove_custom_response(self, trigger):
        if trigger in self.custom_responses:
            del self.custom_responses[trigger]
        else:
            print(f"No custom response found for trigger: {trigger}")

    def get_custom_response(self, trigger):
        if trigger in self.custom_responses:
            return self.custom_responses[trigger]
        else:
            print(f"No custom response found for trigger: {trigger}")

    def list_custom_responses(self):
        return self.custom_responses

# Sample Usage
# custom_responses = CustomizableResponses()
# custom_responses.add_custom_response("hello", "Hello, how can I assist you?")
# custom_responses.add_custom_response("bye", "Goodbye! Have a great day.")
# print(custom_responses.get_custom_response("hello"))
# print(custom_responses.get_custom_response("bye"))
# print(custom_responses.list_custom_responses())
```