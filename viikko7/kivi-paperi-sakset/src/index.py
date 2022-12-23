from kps_peli import KPSPeli



def main():
    while True:
        kpspeli = KPSPeli()
        vaihtoehdot = {"a": kpspeli.ihminen().ihminen(), 
                       "b": kpspeli.ihminen().tekoaly(), 
                       "c": kpspeli.ihminen().parannettutekoaly()}

        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in vaihtoehdot.keys():
            vaihtoehdot[vastaus].pelaa()
        else:
            break


if __name__ == "__main__":
    main()
