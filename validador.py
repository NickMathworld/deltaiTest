import json

class ValidadorJSON:
	def carga_JSON(self,entrada):
		data_JSON = {}
		try:
			with open(entrada+'.json') as json_file:
				data_JSON = json.load(json_file)
				respuesta = self.valida_JSON(data_JSON)
				return respuesta
		except:
			return "ERROR AL ABRIR ARCHIVO JSON"
			
	def exporta_JSON(self,entrada,data_out):
		with open(entrada+'_out.json', 'w') as file:
			json.dump(data_out, file, indent=4)

	def valida_JSON(self,data_JSON):
		data = []
		for it in data_JSON:
			if self.valida_tipos(it) and self.contine_propiedades(it):
				data.append(it)
			else:
				return "ERROR AL VALIDAR JSON"

		return data

	def valida_tipos(self,data_JSON):
		respuesta = True
		return respuesta

	def es_numero(self,cadena):
		if type(cadena) == int or type(cadena) == float:
			return True
		else:
			return False
	

	def contine_propiedades(self,data_JSON):
		CAMPOS_REQUERIDOS = ["keywords"]
		for propiedad in CAMPOS_REQUERIDOS:
			if propiedad not in data_JSON:
				return False
		return True