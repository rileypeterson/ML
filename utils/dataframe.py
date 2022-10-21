"""
Expanded set of DataFrame functions.
"""
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
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(tf, path=d)
                name = tf.getnames()[0]
            df = pd.read_csv(os.path.join(d, name))
        return df
