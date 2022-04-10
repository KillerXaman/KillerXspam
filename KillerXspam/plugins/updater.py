import asyncio
import os
import sys
import git
from telethon import events
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, DEV, HEROKU_APP_NAME, HEROKU_API_KEY
from .. import CMD_HNDLR as hl

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/KillerXaman/KillerXspam"
BOT_IS_UP_TO_DATE = "**The Killer X Spam** is up-to-date sur."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "updating your Killer X Spam ..."
)
NEW_UP_DATE_FOUND = "New update found for {branch_name}\n" "`updating your Killer X Spam...`"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "KillerSquad"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #

@KILL.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in DEV:
        text = "__ updating Your KillerXspam Userbots __\n **Type** .ping **After 5min To check I'm On !!**"
        await e.reply(text, parse_mode=None, link_preview=None)



@KILL.on(
    events.NewMessage(pattern="^.update", func=lambda e: e.sender_id in DEV)
)
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME, branch_name=active_branch_name
        ),
    )

    if not changelog:
        await message.edit("`Updation in Progress......`")
        await asyncio.sleep(5)

    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name, changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(branch_name=active_branch_name)

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await KILL.send_message(
            message.chat_id, document="change.log", caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Invalid APP Name. Please set the name of your bot in heroku in the var `HEROKU_APP_NAME.`"
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(KILL, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Please create the var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in `HEROKU_API_KEY` var")


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def deploy_start(KILL, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "__Updated your Killer X Spam successfully sur__ !!!\n\n"
    )
    await remote.push(refspec=refspec)
    await KILL.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
