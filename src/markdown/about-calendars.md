---
date: 2024-07-29
author: Shinji Pons
title: "About Digital Calendars"
---

# About Digital Calendars

Recently I have been thinking about changing calendar apps. Up until now, I have been using Apple Calendar which was adequate but I have been complaining how the lack of a proper Windows desktop client has been a problem.

Yes, I know that Outlook Calendar can support iCloud but after spending two hours figuring out that I had to not use my Apple ID email to get it to work and that I was still having other issues that I will get into later, I decided to look for an alternative.

# My requirements

I am not a very busy guy but I rely on my digital calendar to keep track of few meetings, job interviews, appointments and other life events that I do not want to forget.

I'm a Windows user with an iPhone. My MacBook Pro from 2015 is collecting dust. I need a solution that works on both Windows and iPhone. Browser based solutions are acceptable for Windows but native apps are much preferred.

Here are my requirements:
- Cross platform, Windows and iOS as a bare minimum
- No ads
- No subscription, freemium is ok
- Free/busy status embedded into events
- Repeating events
- Events can be shared with other people
- Adding other calendars such as official holidays and sports events such as Premier League fixtures and Formula 1 races.

Nice-to-haves:
- have a one-click add to calendar working with my email provider [Proton Mail](https://protonmail.com/).
- integrates with Cal.com

# The problems

Apple Calendar and Google Calendar are the main choices in today's world. They are both popular and solid options but they are not perfect for me.

Apple Calendar offers a very poor experience for Windows users, perhaps willingly so. The web app is decent but nothing out of the ordinary.

!()[media/about-calendars/icloud-web.png]

Its main downsides are:
- lack of dark mode
- text is very small on my 27-in monitor
- impossible to change how many hours are shown inside of the visible screen area
- deleting an event requires a double click to show a modal window that contains the "delete" button
- the typeface used isn't very beautiful

# The obvious candidate: Outlook

But I want to use Outlook's desktop application. Now about that...

!()[media/about-calendars/outlook-desktop.png]

You have **Outlook** and **Outlook (new)**. OK, let's use the new one...

!()[media/about-calendars/outlook-new.png]

The new Outlook always opens on the emails. And on top of that, it shows you an ad at the very top of your inbox! So I'm thinking there must be a way to change it...

!()[media/about-calendars/opening-outlook.png]

Nope that wasn't it. I found out after a few minutes that you need to right-click on the calendar icon in the left sidebar to "pin" the calendar to the task bar.

!()[media/about-calendars/opening-outlook-on-calendar.png]

But at least, you can change the "time scale" very quickly and easily by right-clicking on the time. Very nice!

!(Not the best way to do this...)[media/about-calendars/outlook-time-scale.png]

OK. What about Outlook's iOS application?

I got a error message because the app-specific password you use inside of Outlook must be used with the @icloud.com adress tied to your Apple ID account. If you use the email adress that you use to sign in with your Apple ID, you will get an error! How are you supposed to know that? Well, you DON'T because neither the [Apple Support](https://support.apple.com/en-gb/guide/icloud-windows/icwa12798053/icloud) nor the [Windows support](https://support.microsoft.com/en-gb/office/add-or-manage-an-icloud-email-account-in-outlook-4aed8b3d-3c68-4743-8973-f6bd1c56e040) pages mention that anywhere.

> When I set that up the first time, I remember wasting two hours on this

At first sight, the Outlook app looks too bloated since it comes with its whole suite of email, feeds and apps which I don't need.

!()[media/about-calendars/outlook-ios-app.png]

And as I suspected, there is no way to get the app to open to the Calendar directly. So it's a no-go for me.

!()[media/about-calendars/outlook-ios-impossible.png]

# Looking for more alternatives

So Apple Calendar isn't a viable option because of the Windows experience. On iOS, I used [Fantastical](https://flexibits.com/fantastical) but they don't have a client for Windows.

At this point, I needed a way to find alternatives in a time-efficient manner. Luckily, I stumbled onto [this page inside of the cal.com app](https://flexibits.com/fantastical) that lists a bunch of calendar apps that are compatible with cal.com!

Let's go through them one by one.

1. **Google Calendar:** widely used but I would prefer to not hand Google my data if possible.
2. Outlook Calendar: poor experience on Windows and iOS for me
3. Apple Calendar: poor experience on Windows for me.
4. CalDav: irrelevant.
5. **Notion Calendar:** requires a Google account.
6. **Amie:** requires a Google account.
7. Zoho Calendar: requires adopting into Zoho's ecosystem and its whole suite of apps (email) and iOS calendar experience is bundled with everything else.
8. ICS feed: irrelevant.
9. Vimcal: requires a Google account.
10. Lark Calendar: looks like a bloaty app targeted to businesses.
11. Microsoft Exchange: irrelevant.
12. Microsoft Exchange 2016 Calendar: irrelevant.
13. Microsoft Exchange 2013 Calendar: irrelevant.

# Proton Calendar

So at this point, I'm considering using Google Calendar again. But I remember about [Proton Calendar](https://proton.me/calendar/features). Since it's already part of the suite of Proton applications, maybe it's the solution for me?

Let's check out **Proton Calendar**...

!()[media/about-calendars/proton-calendar.png]

It looks appropriate on the surface but after trying it for a few weeks, I realize that there are more than a few deal-breakers for me.

I'm OK with it being a web app since I use my email only on the web anyway. But I started noticing that some of my emails containing calendar attachements (*.ics files).

Some events can be added at a click of a button, while some others show me a cryptic error message.

!()[media/about-calendars/proton-calendar-add.png]

!()[media/about-calendars/proton-calendar-no-add.png]

On top of that, it's not allowing me to mark certain events as free or busy on a per-event basis inside of the event options:

!()[media/about-calendars/proton-calendar-no-free-busy.png]

After some back and forth with the Proton Mail support team, I was told that my use of SimpleLogin with my shinjipons.com domain, combined disabling my old shinjipons.com email adresses in the Proton Mail settings meant that this error was unavoidable.

The only solutions are to delete the disabled adresses, but that requires deleting all emails which contain those adresses, which is unacceptable; or to stop using those disabled adresses (which I can keep using through SimpleLogin) in favour of new emails adresses only created through SimpleLogin.

I thought about this solution for a while but I would still be missing the collaborative nature of a calendar. I want my calendar to remain private but **everyone else** uses calendar apps that are *collaborative* but **not private**.

# Narrowing down the choices

I wanted to keep using Proton Calendar, but the lack of integration with the ubiquitous calendar apps out there combined with the hiccups of my admittedly using situation with SimpleLogin meant that I was back to considering Google Calendar.

I will be checking out Amie and Notion Calendar in more detail in the coming weeks. Google Calendar does not offer dark mode in the web browser and the iOS app's UI is too blocky.

In Chrome, which I do not use as my daily browser it seems possible to "auto dark mode" web contents using Chrome flags. But I don't think it's a viable or desirable option.

```
chrome://flags
```

Amie's pricing is a bit high and their upselling is too noticeable but on the other hand, their desktop app for Windows is absolutely gorgeous and I noticed that the iOS app does not annoyingly prompt me about editing one instance of a repeating event (although that is useful 5% of the time).

I noticed that inside of **Amie**'s desktop app, it's impossible to add more than one notification for events whereas the Google Calendar settings perfectly allow for that.

!()[media/about-calendars/amie-only-one-reminder.png]

**Notion Calendar** offers something interesting where it presents itself as the "time management app for your life". But both the Windows desktop and iOS apps have some quirks that will take some getting used to, mainly the custom looking notifications on Windows and the slightly buggy UI when pinching in/out on iOS.

!()[media/notion-calendar-zoom-bug.mp4]

# Conclusion

So for the next few weeks and months, I will be scoping out **Amie** and **Notion Calendar**. I must admit I already have a preference for Amie. The finishes on the UI and overall product are noticeable compared to Notion Calendar. On the other hand, Notion Calendar offers an experience with less intrusive upselling, collaborative features that are slightly easier to discover and integration to Notion out of the box (great for taking notes related to meetings).