import speedtest
import time
import emoji
import textwrap

from termcolor import colored

from src.helpers import system, print_typo


def download_speed():
    retry = 0
    speed = False
    while speed == False and retry <= 3:
        try:
            time.sleep(1)

            speed_test = speedtest.Speedtest()

            download_speed = speed_test.download()

            mbps = download_speed / (1024 * 1024)

            speed = True

        except:
            mbps = "Error"

            retry += 1

    return mbps


def delay(mbps):
    if mbps <= 10:
        wait = 20

    elif mbps <= 25:
        wait = 15

    elif mbps <= 75:
        wait = 10

    else:
        wait = 5

    return wait


def internet_speed_retry():
    is_windows = system()

    internet_retry = True

    while internet_retry == True:
        print("\n\nDetermining internet speed.")

        mbps = download_speed()

        time.sleep(1)

        if mbps == "Error":
            print(
                "\n"
                + colored(" ! ", "yellow", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":loudspeaker:") * (not is_windows)
                + colored(
                    "   It seems that your internet speed is unstable at the moment.",
                    "yellow",
                )
            )

            print(
                "\n"
                + colored(" i ", "blue", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":information:") * (not is_windows)
                + "   Please check your internet connection, and then make a selection."
            )

            print(
                "\n"
                + colored(" i ", "blue", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":information:") * (not is_windows)
                + textwrap.fill(
                    "   Note that an unstable internet connection might interfere with the download process.",
                    100,
                )
            )

            internet_typo = True

            while internet_typo:
                internet_option = input(
                    colored(
                        "\n-- Type [1] to retry speed check\n-- Type [2] to continue with an unstable connection\n   : "
                    )
                )

                if internet_option == "1":
                    internet_typo = False
                elif internet_option == "2":
                    mbps = 15
                    internet_typo = False
                    internet_retry = False
                else:
                    print_typo()

        elif mbps <= 5:
            print(
                "\n"
                + colored(" ! ", "yellow", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":loudspeaker:") * (not is_windows)
                + colored("   Your internet speed is less than 5 mbps.", "yellow")
            )

            print(
                "\n"
                + colored(" i ", "blue", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":information:") * (not is_windows)
                + "   Please check your internet connection, and then make a selection."
            )

            print(
                "\n"
                + colored(" i ", "blue", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":information:") * (not is_windows)
                + textwrap.fill(
                    "   Note that a slow internet connection might interfere with the upload and download process.",
                    100,
                )
            )

            internet_typo = True

            while internet_typo:
                internet_option = input(
                    colored(
                        "\n-- Type [1] to retry speed check\n-- Type [2] to continue with a slow connection\n   : "
                    )
                )

                if internet_option == "1":
                    internet_typo = False
                elif internet_option == "2":
                    mbps = 15
                    internet_typo = False
                    internet_retry = False
                else:
                    print_typo()

        else:
            print(
                "\n"
                + colored(" ! ", "green", attrs=["reverse"]) * (is_windows)
                + emoji.emojize(":check_mark_button:") * (not is_windows)
                + colored(
                    "   Your internet speed is: " + str(round(mbps, 2)) + " mbps\n",
                    "green",
                )
            )

            internet_retry = False

    return mbps
