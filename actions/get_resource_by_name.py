import json
from lib import action


class GetResourceByName(action.vRealizeAutomationAction):
    def run(self, resourceName):
        resource = self.vra7.getResourceByName(name=resourceName)
        data = json.dumps(resource)
        jsondata = json.loads(data)
        resourceId = jsondata["id"]
        resourceDetail = self.vra7.getResource(id=resourceId, show='json')
        return json.dumps(resourceDetail)
