nama = "Andhika Widjaja"

umur = 27

background = {
    "edukasi": "S1",
    "keluaga": "berkeluarga",
    "mencari_pekerjaan": True,
    "tahun_lahir": 1996
}

makanan_fav = ["apel", "nasi goreng"]


def marah():
    print("HEI")


def kenalan():
    print("nama saya", nama)
    print("saya lahir di tahun", background['tahun_lahir'])
    print("salam kenal")


def makan(makanan):
    if (makanan.lower() in makanan_fav):
        print("YAY makan enak", makanan)
    else:
        print("makan", makanan)


if (__name__ == '__main__'):
    print("halo saya andi")
    import sys
    inputs = sys.argv
    if (len(inputs) > 2):
        if (inputs[1] == 'makan'):
            makan(inputs[2])
