import DownloadEAFC24 as d_eafc24

def Main():
    url_origineafc24 = "https://prod.cloudflare.cdn.ea.com/published/eamaster/s/shift/fc/fc_24/patch__ww_x0_patchb/fc_24pcpatch__ww_x0_patchbconcept_125__phoenixwwretail78826429235397a16794809bf7565700ce1bf79.zip?verify=1758006779-kC6K6zs%2BnqE1Nb6pOCE%2Fq0gqjzbFHK1jN2aeIff69do%3D"
    output = "EAFC24_PCFullVersion.zip"
    d_eafc24.DownloadEAFC24(url=url_origineafc24, output_path=output)

if __name__ == "__main__":
    Main()
