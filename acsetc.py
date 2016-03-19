
def constructdata(obsfilter1,obsfilter2,normfilter,normmag,ext,exptime):
        
    data = {
        "detector":"wfc",
        "wfcfilt0":obsfilter1,
        "wfcfilt1":obsfilter2,
        "hrcfilt0":"CLEAR1S",
        "hrcfilt1":"CLEAR2S",
        "sbcfilt0":"F115LP",
        "gain": "2.0",
        "crsplit":"4",
        "post_flash_acs":"0",
        "simmode":"SNR",
        "Time":str(exptime),
        "SNR":"10.0",
        "fsourceType":"point",
        "xRegionType":"default",
        "extractionRegionSquare":"5",
        "extractionRegionCircle":"0.2",
        "extractionRegionUserCircle":"0.4",
        "extractionRegionVariableCircle":"80.0",
        "fdiameter":"8",
        "xRegionExtendedType":"Square",
        "extractionRegionExtendedSquare":"5",
        "extractionRegionExtendedCircle":"0.4",
        "extractionRegionExtendedUserCircle":"0.4",
        "fOtherFile":"",
        "fSpectrumCK":"O3V",
        "fSpectrumPickles":"O5V",
        "fsorigin":"SpectrumKurucz",
        "fbpgsfile":"K0V",
        "fStellar":"O5_V",
        "fcalfile":"AGK+81D266",
        "fnonstellar":"Gliese 229B",
        "fbbtemp":"10000",
        "fIndex":"-1",
        "fIsLambda":"true",
        "febmvtype":"mwavg",
        "febv":str(ext),
        "fextinctiontype":"before",
        "fRedshift":"0.0",
        "fL1_center":"0",
        "fL1_fwhm":"0.",
        "fL1_flux":"0.",
        "fL2_center":"0.",
        "fL2_fwhm":"0.",
        "fL2_flux":"0.",
        "fL3_center":"0.",
        "fL3_fwhm":"0.",
        "fL3_flux":"0.",
        "fftype":"fnormalize.bandpass",
        "rn_flux_bandpass_units":"vegamag",
        "rn_flux_bandpass":str(normmag),
        "fftype_filters":"fNormalizeByFilter.wfc3UVIS",
        "filter.ubvri":"Johnson/V",
        "filter.sloan":"Sloan/R",
        "filter.nicmos":"NICMOS/F110W",
        "filter.acs":"ACS/F435W",
        "filter.wfc3UVIS":normfilter,
        "filter.wfc3IR":"WFC3/IR/F098M",
        "rn_flux_lambda":"1.5e-13",
        "rn_flux_lambda_units":"flam",
        "rn_lambda":"5500",
        "rn_lambda_units":"angstroms",
        "ZodiSpec":"ZodiStandard",
        "ZodiStandard":"Average",
        "ZodiRA":"00:00:00",
        "ZodiDec":"+00:00:00",
        "ZodiSunAttribute":"SunAngle",
        "ZodiSun":"90",
        "ZodiSunAttribute":"Date",
        "ZodiDate":"2009",
        "ZodiMonth":"1",
        "ZodiDay":"1",
        "ZodiMag":"30.0",
        "ZodiMult":"1.0",
        "EarthshineSpec":"EarthshineStandard",
        "EarthshineStandard":"None",
        "EarthshineMag":"30.0",
        "EarthshineMult":"1.0",
        "AirglowStandard":"None",
        "instrument":"acs",
        "science_mode":"imaging"
    }
    return data

def place_acs_request(data):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0'}

    s=requests.Session()
    req = requests.Request('POST', "http://etc.stsci.edu/etc/calculate/acs/imaging", data=data, headers=headers)
    prepped=req.prepare()
    resp=s.send(prepped)
    body=resp.content
    nn=body.find("SNR = ")
    ff=body[nn:-1].find("\n")
    snr=body[nn+6:nn+ff].replace(",","")
    return snr


def acsetc(obsfilter1,obsfilter2,normfilter,normmag,ext,exptime):
    data=constructdata(obsfilter1,obsfilter2,normfilter,normmag,ext,exptime)
    the_page=place_acs_request(data)

    return the_page
#------------------------------------------------------------------------------
# main
#
def _main():
    import sys
    """
    This is the main routine.
    """
    if (len(sys.argv)<7):
        print("acs3etc.py obs_filter1 obs_filter2 norm_filter norm_vega_mag extinction exptime")
        return
    
    print(acsetc(sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])))
    
#------------------------------------------------------------------------------
# Start program execution.
#
if __name__ == '__main__':
    _main()




