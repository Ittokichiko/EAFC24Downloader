import DownloadEAFC24 as d_eafc24

def Main():
    url_origineafc24 = "https://origin-a.akamaihd.net/eamaster/s/shift/fc/fc_24/patch__ww_x0_patchb/fc_24pcpatch__ww_x0_patchbconcept_125__phoenixwwretail78826429235397a16794809bf7565700ce1bf79.zip?sauth=1758008968_e7f3d1699cf7f0a77f36fcb45c7ebde7"
    output = "EAFC24_PCFullVersion.zip"
    d_eafc24.DownloadEAFC24(url=url_origineafc24, output_path=output)

if __name__ == "__main__":
    Main()