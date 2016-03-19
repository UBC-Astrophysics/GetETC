
def constructdata(obsfilter,normfilter,normmag,ext,exptime):
        
    data = {
        "wfc3_filter_type" : "wide",
        "wfc3_filter_w" : obsfilter,
        "wfc3_filter_m":"F390M", 
        "wfc3_filter_n":"F280N",
        "wfc3_filter_q":"FQ232N",
        "gain": "1.5",
        "crsplit":"1",
        "detector":"uvis2",
        "post_flash_wfc3":"0",
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
        "instrument":"wfc3uvis",
        "science_mode":"imaging"
    }
    return data

def place_uviswfc3_request(data):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0'}

    s=requests.Session()
    req = requests.Request('POST', "http://etc.stsci.edu/etc/calculate/wfc3uvis/imaging", data=data, headers=headers)
    prepped=req.prepare()
    resp=s.send(prepped)
    body=resp.content
    nn=body.find("SNR = ")
    ff=body[nn:-1].find("\n")
    snr=body[nn+6:nn+ff].replace(",","")
    return snr


def uviswfc3etc(obsfilter,normfilter,normmag,ext,exptime):
    data=constructdata(obsfilter,normfilter,normmag,ext,exptime)
    the_page=place_uviswfc3_request(data)

    return the_page
#------------------------------------------------------------------------------
# main
#
def _main():
    import sys
    """
    This is the main routine.
    """
    if (len(sys.argv)<6):
        print("uviswfc3etc.py obs_filter norm_filter norm_vega_mag extinction exptime")
        return
    
    print(uviswfc3etc(sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])))
    
#------------------------------------------------------------------------------
# Start program execution.
#
if __name__ == '__main__':
    _main()




