library(pacman)
pacman::p_load(tidyverse, ggplot2, readr)

#setwd('/Users/hannahdenobrega/Documents/FoP_bin/pages')
setwd("./pages")

df <- read_csv("data/seasonal_data.csv")

plot_seasonally_adjusted <- df %>% 
  ggplot() + 
  geom_line(aes(Date, value_sa), color = "steelblue") +
  # facet_wrap(~ticker, scales = "free_y") + 
  ggthemes::theme_economist() + 
  ggthemes::scale_color_economist() #+ theme_bw()+ 
  labs(
    x = "",
    y = "",
    #colour = "Fruit",
    title = "Fruit seasonally adjusted"
  ) +
  theme(
    plot.title = element_text(face = "bold", size = 12),
    legend.background = element_rect(fill = "white", size = 4, color = "white"),
    legend.justification = c(0, 1),
    legend.position = c(0, 1),
    axis.ticks = element_line(color = "grey70", size = 0.2),
    panel.grid.major = element_line(color = "grey70", size = 0.2),
    panel.grid.minor = element_blank()
  ) 

ggsave("plots/plot_seasonally_adjusted.png", width = 8, height = 6)

