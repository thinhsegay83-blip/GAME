extends CharacterBody2D
## Nhan vat nguoi choi: di chuyen 8 huong, quay mat theo huong di.

## Thu tu trung voi thu tu khung hinh trong player_tam.png
enum Facing { DOWN, UP, LEFT, RIGHT }

## Toc do di bo, px/giay. 80 px/s = 5 o/giay voi o 16 px.
const SPEED := 80.0

var facing: Facing = Facing.DOWN

@onready var sprite: Sprite2D = $Sprite2D
@onready var camera: Camera2D = $Camera2D


func _physics_process(_delta: float) -> void:
	var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = direction * SPEED
	move_and_slide()
	if direction != Vector2.ZERO:
		_update_facing(direction)


func _update_facing(direction: Vector2) -> void:
	if absf(direction.x) > absf(direction.y):
		facing = Facing.RIGHT if direction.x > 0.0 else Facing.LEFT
	else:
		facing = Facing.DOWN if direction.y > 0.0 else Facing.UP
	sprite.frame = facing


## Gioi han camera trong pham vi ban do (don vi px).
func set_camera_limits(bounds: Rect2i) -> void:
	camera.limit_left = bounds.position.x
	camera.limit_top = bounds.position.y
	camera.limit_right = bounds.end.x
	camera.limit_bottom = bounds.end.y
