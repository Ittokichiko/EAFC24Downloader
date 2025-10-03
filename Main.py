import DownloadEAFC24 as d_eafc24
import Music
def Main():
    url_origineafc24 = "https://origin-a.akamaihd.net/eamaster/s/shift/fc/fc_24/patch__ww_x0_patchb/fc_24pcpatch__ww_x0_patchbconcept_125__phoenixwwretail78826429235397a16794809bf7565700ce1bf79.zip?sauth=1759620766_003e2a00714ee8a6dc2d7f0cbec36196"
    output = "EAFC24_PCFullVersion.zip"
    Music.PlayMusic("TheNightsAvicii.mp3")
    d_eafc24.DownloadEAFC24(url=url_origineafc24, output_path=output)

if __name__ == "__main__":
    Main()
