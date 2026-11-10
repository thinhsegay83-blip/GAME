extends Node
## Autoload "Game": thiet lap dung chung cho ca game.
## Hien tai chi dang ky phim dieu khien. Dang ky bang code thay vi sua tay
## trong project.godot de de doc va khong phu thuoc phien ban Godot.

const ACTIONS := {
	"move_left": [KEY_A, KEY_LEFT],
	"move_right": [KEY_D, KEY_RIGHT],
	"move_up": [KEY_W, KEY_UP],
	"move_down": [KEY_S, KEY_DOWN],
	"interact": [KEY_E],
}


func _ready() -> void:
	_register_input_actions()


func _register_input_actions() -> void:
	for action in ACTIONS:
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		for keycode in ACTIONS[action]:
			var event := InputEventKey.new()
			# physical_keycode: theo vi tri phim, khong phu thuoc bo go
			event.physical_keycode = keycode
			InputMap.action_add_event(action, event)
