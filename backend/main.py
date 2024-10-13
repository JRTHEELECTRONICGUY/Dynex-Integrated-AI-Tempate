from dynex_api import process_request, compute_cycle
from storage_manager import save_to_drive, save_in_memory

def handle_request(api_key, user_data, storage_option="memory"):
    if not validate_api_key(api_key):
        return {"error": "Invalid API key"}

    try:
        response = process_request(user_data)
        if storage_option == "drive":
            save_to_drive(response)
        else:
            save_in_memory(response)

        compute_cycle(api_key)
        return {"status": "success", "data": response}
    except Exception as e:
        return {"error": str(e)}

def validate_api_key(api_key):
    # Simulate API key validation
    valid_keys = ["TEST_KEY_123"]
    return api_key in valid_keys
