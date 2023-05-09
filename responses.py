import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'what about you??':
        return ' im fine as always!'

    if p_message == 'what about u':
        return ' im fine as always!'

    if p_message[0] == 'h':
        return 'Hey! how are you?!'

    if p_message == 'fine':
        return 'Thats great'

    if p_message == 'good':
        return 'Thats wonderful'

    if p_message == 'great':
        return 'fantastic'

    if p_message == 'bad':
        return 'Nothing is wrong, you must stay confident and keep pushing to stay healthy.'

    if p_message == 'sad':
        return 'Cmoon! dont be sad, Im always there for you.'

    if p_message == 'angry':
        return 'Calm yourself, your not the only one who can get angry.'

    if p_message == 'frustrated':
        return 'Frustration can cause anger and anger is immature... stay calm'

    if p_message == 'depressed':
        return 'Dont be depressed! cheer up ! because even in the face of depression u can move on'

    if p_message == 'thanks':
        return 'your welcome'

    if p_message == 'thank you':
        return 'your welcome'

    if p_message == 'thnx':
        return 'your welcome'

    if p_message == 'im fine':
        return 'Thats great'

    if p_message == 'im good':
        return 'Thats great'

    if p_message == 'im great':
        return 'Thats great'

    if p_message == 'bad':
        return 'Nothing is wrong, you must stay confident and keep pushing to stay healthy.'

    if p_message == 'im sad':
        return 'Cmoon! dont be sad, Im always there for you.'

    if p_message == 'im angry':
        return 'Calm yourself, your not the only one who can get angry.'

    if p_message == 'im frustrated':
        return 'Frustration can cause anger and anger is immature... stay calm'

    if p_message == 'im depressed':
        return 'Dont be depressed! cheer up ! because even in the face of depression u can move on'

    if p_message == 'roll a dice':
        return str(random.randint(1, 6))
