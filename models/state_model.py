
from observer import Observable


class StateModel(Observable):

    def __init__(self):
        super().__init__()
        self._state = ''

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, input_value):
        self._state = input_value
        self.notify_all(state=input_value)