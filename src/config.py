from pathlib import Path
import os


class Config:
    DEFAULT_DATAPATH: Path = Path("data/")

    def __init__(self, data_path: str | None = None) -> None:
        self.root: Path = Path(os.getcwd())

        if data_path is not None:
            self.data_path = Path(os.path.join(self.root, data_path))
        else:
            self.data_path = Path(os.path.join(self.root, self.DEFAULT_DATAPATH))

    def set_datapath(self, path: str) -> None:
        """set_datapath is a method that change the default data folder for search databases.

        Args:
            path (str): New path name (relative to the app.py)

        Sample:
            config = Config()
            config.set_datapath("folders/newdatafolder/")

        TODO: confirm that path exists (or create it)
        """
        self.data_path = Path(os.path.abspath(path))
