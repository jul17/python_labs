from app import ma


class Structure(ma.Schema):
    class Meta:
        fields = ('id', 'musicInstrumentprice', 'Priece', 'countruFrom')