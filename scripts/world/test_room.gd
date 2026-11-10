extends Node2D
## Phong thu cho M1: doc ban do ky tu tu file .txt, ve san/tuong va tao va cham.
## Chi la khung tam. Sang M2 se thay bang TileMapLayer + tileset that.
##
## Ky hieu ban do:  "#" tuong   "." san   "P" vi tri xuat phat

const TILE := 16
const MAP_PATH := "res://data/maps/test_room.txt"
const WALL := "#"
const SPAWN := "P"

const FLOOR_TEX: Texture2D = preload("res://assets/placeholder/floor_tam.png")
const WALL_TOP_TEX: Texture2D = preload("res://assets/placeholder/wall_top_tam.png")
const WALL_FACE_TEX: Texture2D = preload("res://assets/placeholder/wall_face_tam.png")

var _rows: PackedStringArray = PackedStringArray()
var _spawn_cell := Vector2i(1, 2)


func _ready() -> void:
	_load_map()
	_build_collision()
	queue_redraw()


func _draw() -> void:
	for y in _rows.size():
		var row := _rows[y]
		for x in row.length():
			var pos := Vector2(x * TILE, y * TILE)
			if row[x] != WALL:
				draw_texture(FLOOR_TEX, pos)
			elif _is_wall(x, y + 1):
				# Phia duoi van la tuong: chi thay mat tren
				draw_texture(WALL_TOP_TEX, pos)
			else:
				# Phia duoi la san: thay mat truoc cua tuong (goc nhin 3/4)
				draw_texture(WALL_FACE_TEX, pos)


## Vi tri xuat phat cua nguoi choi (px), tinh tai tam o.
func get_spawn_position() -> Vector2:
	return Vector2(_spawn_cell * TILE) + Vector2(TILE / 2.0, TILE / 2.0)


## Pham vi ban do (px), dung de gioi han camera.
func get_bounds() -> Rect2i:
	var width := 0
	for row in _rows:
		width = maxi(width, row.length())
	return Rect2i(0, 0, width * TILE, _rows.size() * TILE)


func _load_map() -> void:
	var file := FileAccess.open(MAP_PATH, FileAccess.READ)
	if file == null:
		push_error("Khong mo duoc ban do: %s" % MAP_PATH)
		return
	while not file.eof_reached():
		var line := file.get_line().strip_edges()
		if not line.is_empty():
			_rows.append(line)
	for y in _rows.size():
		var x := _rows[y].find(SPAWN)
		if x != -1:
			_spawn_cell = Vector2i(x, y)


## Ngoai pham vi ban do duoc coi la tuong, de hang tuong duoi cung hien mat tren.
func _is_wall(x: int, y: int) -> bool:
	if y < 0 or y >= _rows.size():
		return true
	if x < 0 or x >= _rows[y].length():
		return true
	return _rows[y][x] == WALL


## Gop cac o tuong lien nhau tren cung mot hang thanh 1 hinh chu nhat va cham.
func _build_collision() -> void:
	var body := StaticBody2D.new()
	body.name = "Walls"
	add_child(body)
	for y in _rows.size():
		var row := _rows[y]
		var run_start := -1
		for x in row.length() + 1:
			var wall_here := x < row.length() and row[x] == WALL
			if wall_here and run_start == -1:
				run_start = x
			elif not wall_here and run_start != -1:
				_add_wall_shape(body, run_start, y, x - run_start)
				run_start = -1


func _add_wall_shape(body: StaticBody2D, cell_x: int, cell_y: int, length: int) -> void:
	var shape := RectangleShape2D.new()
	shape.size = Vector2(length * TILE, TILE)
	var collider := CollisionShape2D.new()
	collider.shape = shape
	collider.position = Vector2(cell_x * TILE, cell_y * TILE) + shape.size / 2.0
	body.add_child(collider)
