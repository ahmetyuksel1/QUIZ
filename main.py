import colorama
from colorama import Fore, Back, Style

print(Fore.BLUE, "\nlearnEN İngilizce uygulamasına hoşgeldiniz.\n"
                 "Bu uygulamada konu anlatımından, İngilizce kelime öğrenmeye "
                 "hatta İngilizce genel kültür sorularını yanıtlamak gibi etkinliklere göz atabilirsiniz.", Style.RESET_ALL)

while True:
    try:
        print(Fore.BLUE, "\nİngilizce'de zamanlarla ilgili konu anlatımı için '1',\n"
                      "günlük hayattan İngilizce kelimeler ve Türkçe karşılıkları için '2',\n"
                      "İngilizce çoktan seçmeli genel kültür sorularını yanıtlamak için '3',\n"
                      "Uygulamadan çıkmak için herhangi bir tuşa basın. ", Style.RESET_ALL)

        giris = input("\nSeçiminiz: ")

        if giris == "1":
            import lecture
        elif giris == "2":
            import words
        elif giris == "3":
            import quiz
        else:
            print(Fore.RED, "\nSeçim geçersiz, uygulama sonlandırıldı.", Style.RESET_ALL)
            print(Fore.YELLOW, "\nlearnEN - Ahmet YÜKSEL 1214225018 - Bilgiyle kalın!", Style.RESET_ALL)
            exit()

    except ValueError:
        print("\nGirilen değer hatalı. Program sonlandırıldı.")
        break
    except IndexError:
        print("\nGirilen indeks hatalı. Program sonlandırıldı.")
        break
