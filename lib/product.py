import os
import json

class Product:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.model_path = os.path.join(folder_path, "model.onnx")
        if not os.path.isfile(self.model_path):
            self.model_path = None

        self.info = None
        self.info_path = os.path.join(folder_path, "info.json")
        if not os.path.isfile(self.info_path):
            self.info_path = None
        else :
            with open(self.info_path, "r") as json_result:
                self.info = json.load(json_result)

        self.represent_neg = self._make_data_path(True)
        self.represent_pos = self._make_data_path(False)


    def _make_data_path(self, is_neg):
        path = os.path.join(self.folder_path, "test", "neg" if is_neg else "pos")
        return os.path.join(path, os.listdir(path)[0])