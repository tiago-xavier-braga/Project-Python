import folium

pampulha = folium.Map(
	location = [-16.709688, -43.835384],
	zoom_start = 16,
	)

folium.Marker(
	[-16.709688, -43.835384],
	tooltip = "Pampulha, click para saber mais",
	popup = "<i>Lagoa Francisco Peres, ponto turístico de Montes Claros</i>",
	).add_to(pampulha)

pampulha.save("pampulha_montes_claros.html")

lapa_grande = folium.Map(
	location = [-16.727409, -43.961818],
	zoom_start = 12,
	tiles="Stamen Terrain"
	)

folium.CircleMarker(
	location = [-16.727409, -43.961818],
	radius = 160,
	popup = "Parque Lapa Grande",
	color = "#3186cc",
	fill = True,
	).add_to(lapa_grande)

folium.Marker(
	[-16.727409, -43.961818],
	tooltip = "Lapa Grande, click para saber mais",
	popup = "<i>Parque Estadual da Lapa Grande</i>",
	).add_to(lapa_grande)

lapa_grande.save("lapa_grande.html")