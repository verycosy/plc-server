import os
import json

class Product:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.model_path = os.path.join(folder_path, "model.onnx")
        self.info_path = os.path.join(folder_path, "info.json")

        self.represent_neg = self._make_data_path(True)
        self.represent_pos = self._make_data_path(False)

        with open(self.info_path, "r") as json_result:
            self.info = json.load(json_result)


    def _make_data_path(self, is_neg):
        path = os.path.join(self.folder_path, "neg" if is_neg else "pos")
        return os.path.join(path, os.listdir(path)[0])