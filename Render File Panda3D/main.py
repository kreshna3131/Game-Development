# Digunakan Untuk mengimport library yang dibutuhkan
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

# Digunakan Untuk membuat class yang dipakai untuk merender pandas3d


class Mygame(ShowBase):
    # Digunakan untuk membuat fungsi
    def __init__(self):
        # Digunakan untuk mengembalikan ke pada kelas super atau besar
        super().__init__()

        # Digunakan untuk mendeklarasikan nilai mobil yang didalamnya berisi file 3d
        mobil = self.loader.loadModel("image/mobil.egg")
        # Digunakan untuk mendeklarasikan nilai posisi gambar 3d yang diload
        mobil.setPos(0, 10, 0)
        # Digunakan untuk mendeklarasikan ukuran dari gambar 3d yang diload
        mobil.setScale(0.2, 0.2, 0.2)
        # Digunakanuntuk merender gambar 3d yang sudah dideklarasikan
        mobil.reparentTo(self.render)


# Digunakan untuk mendeklarasikan class menjadi class yang akan dijalankan
game = Mygame()
# Digunakan untuk menjalankan game yang sudah dideklarasikan dengan class mygame
game.run()
