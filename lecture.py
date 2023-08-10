import keyboard
import colorama
from colorama import Fore, Back, Style

print(Fore.BLUE, "\nİngilizce dersi için düzenli zamanlar ile ilgili bir programdır.\nProgramı kapatmak için değer aralığı dışında bir seçenek girin.", Style.RESET_ALL)

while True:
    # Yalın zamanlar - The simple tenses
    presentSimple = "Geniş Zaman (Present Simple)\nŞimdiki zamanlarda var olan, her zaman doğru olan veya düzenli olarak yapılan şeyler ve görüşlerle inançlar için kullanılır.\nI/we/you/they arrive(do not arrive)\nhe/she/it arrives(does not arrive)"
    pastSimple = "Di'li Geçmiş Zaman (Past Simple)\nTamamlanan eylemler ve geçmişteki olaylar için kullanılır.\nI/we/you/they arrived(did not arrive)\nhe/she/it arrived(did not arrive)"
    futureSimple = "Gelecek Zaman (Future Simple)\nGelecekteki eylemler ve olaylar için kullanılır.\nI/we/you/they will arrive(will not arrive)\nhe/she/it will arrive(will not arrive)"
    presentPerfect = "Present Perfect\nBir olayın şu andaki zamandan bir süre önce olduğunu veya o eylemin tamamlandığını göstermek için kullanılır.\nI/we/you/they have arrived(have not arrived)\nhe/she/it has arrived(has not arrived)"
    pastPerfect = "Miş'li Geçmiş Zaman (Past Perfect)\nGeçmişteki belirli bir zamandan önce bir olayın olduğunu veya aksiyonun tamamlandığını göstermek için kullanılır.\nI/we/you/they had arrived(had not arrived)\nhe/she/it had arrived(had not arrived)"
    futurePerfect = "Gelecekte Bitmişlik (Future Perfect)\nBir şeyin gelecekteki belirli bir zamandan önce tamamlanacağını göstermek için kullanılır.\nI/we/you/they will have arrived(will not have arrived)\nhe/she/it will have arrived(will not have arrived)"
    # Kesintisiz/ilerleyici zamanlar - The continuous/ progressive tenses
    presentContinuous = "Şimdiki Zaman (Present Continuous/Progressive)\nŞimdi olan veya gelişen eylemler veya olaylar, gelecek planları veya bir olayın tekrarlandığını göstermek için kullanılır.\nI am arriving(am not arriving)\nwe/you/they are arriving(are not arriving)\nhe/she/it is arriving(is not arriving)"
    pastContinuous = "Geçmiş Zamanda Süreklilik (Past Continuous/Progressive)\nGeçmişteki, henüz bitmemiş veya kesintiye uğramış eylemler veya olaylar için kullanılır.\nI/he/she/it was arriving(was not arriving)\nwe/you/they were arriving(were not arriving)"
    futureContinuous = "Gelecek Zamanda Süreklilik (Future Continuous/Progressive)\nGelecekte olacak ve gelecekte devam edecek eylemler veya olaylar için kullanılır.\nI/he/she/it will be arriving(will not be arriving)\nwe/you/they will be arriving(will not be arriving)"
    presentPerfectContinuous = "Present Perfect Continuous/Progressive\nGeçmişte başlamış ve halen devam eden eylemler veya olaylar veya yakın zaman önce biten ve etkileri şimdi görülen geçmişteki eykemler için kullanılır.\nI/we/you/they have been arriving(have not been arriving)\nhe/she/it has been arriving(has not been arriving)"
    pastPerfectContinuous = "Past Perfect Continuous/Progressive\nBir süre için olmuş fakat geçmişteki belirli bit zamandan önce tamamlanmış eylemler veya olaylar için kullanılır.\nI/we/you/they had been arriving(had not been arriving)\nhe/she/it had been arriving(had not been arriving)"
    futurePerfectContinuous = "Future Perfect Continuous/Progressive\nGelecekteki belirli bir zamanda halihazırda gerçekleşiyor olacak eylemler veya olaylar için kullanılır.\nI/we/you/they will have been arriving(will not have been arriving)\nhe/she/it will have been arriving(will not have been arriving)"

    # Değişkenler listesi
    degiskenler = [presentSimple, pastSimple, futureSimple, presentPerfect, pastPerfect, futurePerfect,
                   presentContinuous, pastContinuous, futureContinuous, presentPerfectContinuous, pastPerfectContinuous, futurePerfectContinuous]

    # Kullanıcıya seçenekleri sunalım
    print(Fore.BLUE, "\nLütfen bir konu seçin:\n1- Present Simple, 2- Past Simple, 3- Future Simple, 4- Present Perfect, 5- Past Perfect, 6- Future Perfect\n7- Present Continuous, 8- Past Continuous, 9- Future Continuous, 10- Present Perfect Continuous, 11- Past Perfect Continuous, 12- Future Perfect Continuous", Style.RESET_ALL)

    try:
        # Kullanıcının seçimini alalım
        secim = int(input("Seçiminiz (1-12 arası bir sayı girin): "))

        # Seçilen değişkeni yazdıralım
        print(Fore.BLUE, "Seçim:", Style.RESET_ALL + Fore.LIGHTBLUE_EX, str(secim), Style.RESET_ALL + "\n" + Fore.YELLOW, degiskenler[secim - 1], Style.RESET_ALL)

        if secim == 0:
            print(Fore.RED, "\nGirilen değer '0'. Program sonlandırıldı.\n", Style.RESET_ALL)
            break

    except ValueError:
        print(Fore.RED, "\nGirilen konu numarası bir sayı değil. Program sonlandırıldı.\n", Style.RESET_ALL)
        break
    except IndexError:
        print(Fore.RED, "\nGirilen konu numarası hatalı. Program sonlandırıldı.\n", Style.RESET_ALL)
        break