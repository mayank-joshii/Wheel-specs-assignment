from rest_framework import serializers
from .models import *


class wheelSpecsFormSerializer(serializers.ModelSerializer):

    form_fields = serializers.SerializerMethodField(source='fields')

    class Meta:
        model = wheelSpecsForm
        fields = [
            'form_number', 'submitted_by', 'submitted_date', 'status', 'form_fields'
        ]
    def get_form_fields(self, obj):
        return {
            "treadDiameterNew": obj.tread_diameter_new,
            "lastShopIssueSize": obj.last_shop_issue_size,
            "condemningDia": obj.condemning_dia,
            "wheelGauge": obj.wheel_gauge,
            "variationSameAxle": obj.variation_same_axle,
            "variationSameBogie": obj.variation_same_bogie,
            "variationSameCoach": obj.variation_same_coach,
            "wheelProfile": obj.wheel_profile,
            "intermediateWWP": obj.intermediate_wwp,
            "bearingSeatDiameter": obj.bearing_seat_diameter,
            "rollerBearingOuterDia": obj.roller_bearing_outer_dia,
            "rollerBearingBoreDia": obj.roller_bearing_bore_dia,
            "rollerBearingWidth": obj.roller_bearing_width,
            "axleBoxHousingBoreDia": obj.axle_box_housing_bore_dia,
            "wheelDiscWidth": obj.wheel_disc_width
        }

class WheelSpecsFormCreateSerializer(serializers.ModelSerializer):
    fields = serializers.DictField(write_only=True)

    class Meta:
        model = wheelSpecsForm
        fields = [
            'form_number', 'submitted_by', 'submitted_date', 'fields'
        ]
    
    def create(self, validated_data):
        fields = validated_data.pop('fields', {})
        return wheelSpecsForm.objects.create(
            **validated_data,
            tread_diameter_new=fields.get("treadDiameterNew"),
            last_shop_issue_size=fields.get("lastShopIssueSize"),
            condemning_dia=fields.get("condemningDia"),
            wheel_gauge=fields.get("wheelGauge"),
            variation_same_axle=fields.get("variationSameAxle"),
            variation_same_bogie=fields.get("variationSameBogie"),
            variation_same_coach=fields.get("variationSameCoach"),
            wheel_profile=fields.get("wheelProfile"),
            intermediate_wwp=fields.get("intermediateWWP"),
            bearing_seat_diameter=fields.get("bearingSeatDiameter"),
            roller_bearing_outer_dia=fields.get("rollerBearingOuterDia"),
            roller_bearing_bore_dia=fields.get("rollerBearingBoreDia"),
            roller_bearing_width=fields.get("rollerBearingWidth"),
            axle_box_housing_bore_dia=fields.get("axleBoxHousingBoreDia"),
            wheel_disc_width=fields.get("wheelDiscWidth")
        )