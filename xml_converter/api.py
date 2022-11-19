from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.helpers import xml_to_dict

class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        xml_file = request.FILES.get('file')
        if not xml_file or xml_file.name[-4:] != '.xml':
            return Response(
                {'message': 'Please submit a valid XML file.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        xml_dict = xml_to_dict(xml_file)
        if xml_dict == None:
            return Response(
                {'message': 'Failed to parse provided XML file.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            xml_dict,
            status=status.HTTP_200_OK
        )
