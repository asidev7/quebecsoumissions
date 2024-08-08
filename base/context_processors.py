from base.models import Forfait, Information, Service, Type_Soumission


def getService(request):
    # Récupérer les trois premiers services depuis la base de données
    services = Service.objects.all()
    return {'services':services}

def getSoumission(request):
    soumissions = Type_Soumission.objects.all()
    return {'soumissions':soumissions}

def GetInformation(request):
    information = Information.objects.first()
    return {'information':information}

def GetForfait(request):
    forfaits = Forfait.objects.all()
    return {'forfaits':forfaits}