import os
import json

MODEL_FILE_NAME = "model.onnx"
INFO_FILE_NAME = "info.json"

POSITIVE_FOLDER_NAME = "pos"
NEGATIVE_FOLDER_NAME = "neg"
TEST_FOLDER_NAME = "test"

class Product:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.model_file_path = os.path.join(folder_path, MODEL_FILE_NAME)
        if not os.path.isfile(self.model_file_path):
            self.model_file_path = None

        self.info = None
        self.info_file_path = os.path.join(folder_path, INFO_FILE_NAME)
        if not os.path.isfile(self.info_file_path):
            self.info_file_path = None
        else :
            with open(self.info_file_path, "r") as json_result:
                self.info = json.load(json_result)

        self.represent_neg_image = self._make_image_path(True)
        self.represent_pos_image = self._make_image_path(False)


    def _make_image_path(self, is_negative):
        path = os.path.join(self.folder_path, TEST_FOLDER_NAME, NEGATIVE_FOLDER_NAME if is_negative else POSITIVE_FOLDER_NAME)
        return os.path.join(path, os.listdir(path)[0])