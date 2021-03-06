#ifndef NEWGAMEEVENT_H
#define NEWGAMEEVENT_H

#include "Event.h"

class NewGameEvent : public Event {
  public:
    NewGameEvent(uint32_t event_no, uint32_t maxx, uint32_t maxy,
                 std::vector<std::string> names);


    virtual RawData serialize(bool noCRC = false) override;

    virtual std::string toString(const std::vector<std::string> &names) const override;

    static std::shared_ptr<NewGameEvent> deserialize(RawData data);

    uint32_t getMaxX() const;
    uint32_t getMaxY() const;
    std::vector<std::string> getPlayerNames() const;

    bool operator == (const NewGameEvent &other) const;

  private:
    uint32_t maxx;
    uint32_t maxy;
    std::vector<std::string> playerNames;
};

#endif // NEWGAMEEVENT_H
