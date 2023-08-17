import APIConsume

def save_info(data, path_file):
    f_out = open(path_file,"w")
    f_out.write(data)
    f_out.close()

if __name__ == '__main__':
    PROPS = "MolecularFormula,MolecularWeight,CanonicalSMILES,XLogP,ExactMass,TPSA,Charge,HBondDonorCount,HBondAcceptorCount"

    CID = "2244,2245"

    CAS_ID = "50-78-2"

    URL_PUBCHEM_PATH_SDF = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + CID + "/sdf"

    URL_PUBCHEM_PATH_PROPERTY = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + CID + "/property/" + PROPS + "/CSV"

    URL_CAS_PATH_INFO = "https://commonchemistry.cas.org/api/detail?cas_rn=" + CAS_ID

    save_info(APIConsume.consumeApi(URL_PUBCHEM_PATH_SDF),"mols.sdf")

    save_info(APIConsume.consumeApi(URL_PUBCHEM_PATH_PROPERTY),'pubchem_info.csv')

    save_info(APIConsume.consumeApi(URL_CAS_PATH_INFO),'cas_info.json')

