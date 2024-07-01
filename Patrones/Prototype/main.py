from concrete_prototype import SystemConfigPrototype

def main():
    config = {
        "OS": "Windows",
        "Version": "10",
    }
    original_config = SystemConfigPrototype(config)
    cloned_config = original_config.clone()
    print(f"Original Config: {original_config.configuration}")
    print(f"Cloned Config: {cloned_config.configuration}")

if __name__ == "__main__":
    main()