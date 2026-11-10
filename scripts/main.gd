extends Node2D
## Canh chinh cua M1: dat nguoi choi vao phong thu va gioi han camera.

@onready var room: Node2D = $TestRoom
@onready var player: CharacterBody2D = $Player


func _ready() -> void:
	# _ready cua nut cha chay sau cac nut con, nen phong da doc xong ban do.
	player.global_position = room.get_spawn_position()
	player.set_camera_limits(room.get_bounds())
