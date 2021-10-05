import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class LongitudPalabraFn(beam.DoFn):
    def process(self, element):
        return [len(element)]

palabras = ['Hola', 'Mundo']

with beam.Pipeline(options=PipelineOptions()) as p:
 longs = p | beam.Create(palabras) \
 | beam.ParDo(lambda palabra: [len(palabra)]) \
 | beam.Map(print)