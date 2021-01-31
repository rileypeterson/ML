import tarfile
import tempfile
import urllib.request
import os
import pandas as pd


class DataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def read_tar(cls, url):
        """
        Return a dataframe from a downloadable tarfile url.
        Parameters
        ----------
        url : URL for the tarfile.

        Returns
        -------
        pd.DataFrame
            Output dataframe

        """
        r = urllib.request.urlopen(url)
        with tempfile.TemporaryDirectory() as d:
            with tarfile.open(fileobj=r, mode="r:gz") as tf:
                tf.extractall(path=d)
                name = tf.getnames()[0]
            df = pd.read_csv(os.path.join(d, name))
        return df
