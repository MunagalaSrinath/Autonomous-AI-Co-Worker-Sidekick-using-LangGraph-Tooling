# import gradio as gr
# from sidekick import Sidekick


# async def setup():
#     sidekick = Sidekick()
#     await sidekick.setup()
#     return sidekick


# async def process_message(sidekick, message, success_criteria, history):
#     if not message or not message.strip():
#         return history, sidekick
#     results = await sidekick.run_superstep(message, success_criteria, history)
#     return results, sidekick


# async def reset():
#     new_sidekick = Sidekick()
#     await new_sidekick.setup()
#     return "", "", [], new_sidekick


# def free_resources(sidekick):
#     print("Cleaning up resources...")
#     try:
#         if sidekick:
#             sidekick.free_resources()
#     except Exception as e:
#         print(f"Exception during cleanup: {e}")


# with gr.Blocks(theme=gr.themes.Default(primary_hue="emerald")) as ui:
#     gr.Markdown("## Sidekick Personal Co-Worker")
#     sidekick = gr.State(delete_callback=free_resources)

#     with gr.Row():
#         chatbot = gr.Chatbot(label="Sidekick", height=400, type="messages")

#     with gr.Group():
#         with gr.Row():
#             message = gr.Textbox(
#                 show_label=False,
#                 placeholder="Your request to your sidekick",
#                 lines=2
#             )
#         with gr.Row():
#             success_criteria = gr.Textbox(
#                 show_label=False,
#                 placeholder="What are your success criteria? (optional)",
#                 lines=1
#             )

#     with gr.Row():
#         reset_button = gr.Button("Reset", variant="stop")
#         go_button = gr.Button("Go!", variant="primary")

#     ui.load(setup, [], [sidekick])

#     message.submit(
#         process_message,
#         [sidekick, message, success_criteria, chatbot],
#         [chatbot, sidekick]
#     )

#     success_criteria.submit(
#         process_message,
#         [sidekick, message, success_criteria, chatbot],
#         [chatbot, sidekick]
#     )

#     go_button.click(
#         process_message,
#         [sidekick, message, success_criteria, chatbot],
#         [chatbot, sidekick]
#     )

#     reset_button.click(
#         reset,
#         [],
#         [message, success_criteria, chatbot, sidekick]
#     )

# ui.launch(inbrowser=True)
import gradio as gr
from sidekick import Sidekick


async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick


async def process_message(sidekick, message, success_criteria, history):
    if not message or not message.strip():
        return history, sidekick
    results = await sidekick.run_superstep(message, success_criteria, history)
    return results, sidekick


async def reset():
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", [], new_sidekick


def free_resources(sidekick):
    print("Cleaning up resources...")
    try:
        if sidekick:
            sidekick.free_resources()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


with gr.Blocks() as ui:
    gr.Markdown("## Sidekick Personal Co-Worker")
    sidekick = gr.State(delete_callback=free_resources)

    with gr.Row():
        chatbot = gr.Chatbot(label="Sidekick", height=400)

    with gr.Group():
        with gr.Row():
            message = gr.Textbox(
                show_label=False,
                placeholder="Your request to your sidekick",
                lines=2
            )
        with gr.Row():
            success_criteria = gr.Textbox(
                show_label=False,
                placeholder="What are your success criteria? (optional)",
                lines=1
            )

    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")

    ui.load(setup, [], [sidekick])

    message.submit(
        process_message,
        [sidekick, message, success_criteria, chatbot],
        [chatbot, sidekick]
    )

    success_criteria.submit(
        process_message,
        [sidekick, message, success_criteria, chatbot],
        [chatbot, sidekick]
    )

    go_button.click(
        process_message,
        [sidekick, message, success_criteria, chatbot],
        [chatbot, sidekick]
    )

    reset_button.click(
        reset,
        [],
        [message, success_criteria, chatbot, sidekick]
    )

ui.launch(inbrowser=True, theme=gr.themes.Default(primary_hue="emerald"))