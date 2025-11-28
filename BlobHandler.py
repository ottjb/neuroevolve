from Blob import Blob
from constants import DIR_MOVEMENTS
import random as r

class BlobHandler():
    def __init__(self):
        self.blobs = []

    def update(self):
        for b in self.blobs:
            dir_delta = r.randrange(-2, 3)
            b.pos = tuple(map(sum, zip(b.pos, DIR_MOVEMENTS[b.facing])))
            b.wrap_position()
            b.facing = (b.facing + dir_delta) % 8

    def new_blob(self):
        self.blobs.append(Blob())

    def get_blobs(self):
        return self.blobs

    def get_blob_positions(self):
        positions = []
        for blob in self.blobs:
            positions.append(blob.pos)
        return positions